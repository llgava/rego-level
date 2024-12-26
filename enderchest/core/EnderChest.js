import crypto from 'crypto';
import { Settings } from './utils/Settings.js';
import { Identifier } from './system/Identifier.js';

export class EnderChest {
  static identifier = new Identifier();

  /**
   * Encrypt the specific text to AES.
   * @param {string} text The text to be encrypted.
   * @param {string} iv The Initial Vector value. If not parsed, the Secrete Key Buffer will be used as IV.
   * @returns {string} The encrypted version of the text.
   */
  static encrypt(text, iv = Settings.getKeyBuffer()) {
    const cipher = crypto.createCipheriv(`aes-${Settings.keySize}-cbc`, Settings.getKeyBuffer(), iv);
    let encrypted = cipher.update(text, 'utf-8', 'hex');
    encrypted += cipher.final('hex');
    
    return encrypted;
  }

  /**
   * Decrypt the encrypted text.
   * @param {string} text The encrypted text to be decrypted.
   * @param {string} iv The Initial Vector value. If not parsed, the Secrete Key Buffer will be used as IV.
   * @returns  {string} The decrypted version of the encrypted text.
   */
  static decrypt(text, iv = Settings.getKeyBuffer()) {
    const decipher = crypto.createDecipheriv(`aes-${Settings.keySize}-cbc`, Settings.getKeyBuffer(), iv);
    let decrypted = decipher.update(text.toUpperCase(), 'hex', 'utf-8');
    decrypted += decipher.final('utf-8');

    return decrypted;
  }
}