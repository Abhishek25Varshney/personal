# HTML File Encryption Tool

This tool allows you to encrypt HTML files and create a secure loader that decrypts the content only when the correct password is provided.

## Quick Start

1. **Encrypt your HTML file**
   ```bash
   node encrypt-html.js <input-html-file> <output-txt-file> <your-password>
   ```
   Example:
   ```bash
   node encrypt-html.js test.html test.txt your_password
   ```

2. **Configure the loader**
   - Open `loader.html`
   - Find the placeholder text: `PASTE_YOUR_ENCRYPTED_CONTENT_HERE`
   - Replace it with the encrypted content from your output text file

## How it Works

1. The encryption script (`encrypt-html.js`) takes your HTML file and encrypts it using the provided password
2. The encrypted content is saved to a text file
3. When you paste this content into the loader, it creates a password-protected HTML page
4. Users must enter the correct password to view the decrypted content

## Security Notes

- Choose a strong password that's not easily guessable
- Keep your password secure and separate from the encrypted files
- The encryption is performed client-side using JavaScript
- Do not share your original password with end users

## Files Included

- `encrypt-html.js`: The encryption script
- `loader.html`: The template file for creating password-protected pages

## Requirements

- Node.js installed on your system
- Basic familiarity with command line operations

## Support

For issues or questions, please open an issue in the repository.
