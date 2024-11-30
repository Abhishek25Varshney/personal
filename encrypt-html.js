// encrypt-html.js
const fs = require('fs');

class HTMLEncryption {
    static async encryptHTML(htmlContent, password) {
        const encoder = new TextEncoder();
        const data = encoder.encode(htmlContent);
        
        // Generate key from password
        const keyMaterial = await crypto.subtle.importKey(
            "raw",
            encoder.encode(password),
            "PBKDF2",
            false,
            ["deriveBits", "deriveKey"]
        );
        
        // Generate salt
        const salt = crypto.getRandomValues(new Uint8Array(16));
        
        // Derive key
        const key = await crypto.subtle.deriveKey(
            {
                name: "PBKDF2",
                salt: salt,
                iterations: 100000,
                hash: "SHA-256"
            },
            keyMaterial,
            { name: "AES-GCM", length: 256 },
            false,
            ["encrypt"]
        );
        
        // Generate IV
        const iv = crypto.getRandomValues(new Uint8Array(12));
        
        // Encrypt
        const encrypted = await crypto.subtle.encrypt(
            { name: "AES-GCM", iv: iv },
            key,
            data
        );
        
        // Combine salt + iv + encrypted data
        const encryptedArray = new Uint8Array(encrypted);
        const combined = new Uint8Array(salt.length + iv.length + encryptedArray.length);
        combined.set(salt, 0);
        combined.set(iv, salt.length);
        combined.set(encryptedArray, salt.length + iv.length);
        
        // Convert to base64
        return btoa(String.fromCharCode.apply(null, combined));
    }
}

async function encryptFile(inputFile, outputFile, password) {
    try {
        const htmlContent = fs.readFileSync(inputFile, 'utf8');
        const encrypted = await HTMLEncryption.encryptHTML(htmlContent, password);
        fs.writeFileSync(outputFile, encrypted);
        console.log('File encrypted successfully!');
    } catch (error) {
        console.error('Error encrypting file:', error);
    }
}

if (require.main === module) {
    const args = process.argv.slice(2);
    if (args.length !== 3) {
        console.log('Usage: node encrypt-html.js <input-file> <output-file> <password>');
        process.exit(1);
    }

    const [inputFile, outputFile, password] = args;
    encryptFile(inputFile, outputFile, password);
}
