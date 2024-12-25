import fs from 'fs';
import path from 'path';
import crypto from 'crypto';
import { Settings } from './utils/Settings.js';

export class EnderChest {

  static data = class {
    constructor(original, encrypted, originalPath) {
      const fileName = path.basename(originalPath);

      this.id = EnderChest.data.#generateRandomId();
      this.data = {
        original,
        originalPath,
        encrypted,
        encryptedPath: originalPath.replace(fileName, `${this.id}.json`)
      };
    }

    static #generateRandomId() {
      const n = Math.floor(Math.random() * 90000) + 10000;
      const l = Array.from({ length: 5 }, () =>
        String.fromCharCode(97 + Math.floor(Math.random() * 26))
      ).join('');

      return n + "-" + l;
    }
  }

  static collectAndEncryptIdentifier(path) {
    const rgx = /"identifier"\s*:\s*"([^"]+)"/;
    const rawData = fs.readFileSync(path, 'utf-8');
    const match = rawData.match(rgx);

    if (match) {
      const encrypted = EnderChest.encrypt(match[1]);
      const namespace = encrypted.slice(0, encrypted.length / 2);
      const identifier = encrypted.slice(encrypted.length / 2);

      return new EnderChest.data(match[1], `${namespace}:${identifier}`, path);
    }

    throw new Error(`Missing "identifier" property to the file: ${path}`);
  }

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
    
    return encrypted.toUpperCase();
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