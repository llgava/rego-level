import path from 'path';
import crypto from 'crypto';

export class EnderChestUtils {

  /**
   * Generates a random hash and use it to create an unique ID like XXXX-XXXX
   * @param {string} filePath The original file path of the file.
   * @returns {string} The file path ID.
   */
  static generateFileId(filePath) {
    const hash = crypto.createHash('sha256')
      .update(filePath).digest('hex');
  
    return hash.slice(0, 4) + "-" + hash.slice(-4);
  }

  /**
   * Encrypt the file path to XXXX-XXXX;
   * @param {string} filePath The original file path.
   * @param {string} extension The file extension. Default: json
   * @returns The encrypted file path.
   */
  static encryptFilePath(filePath, extension = 'json') {
    const fileName = path.basename(filePath);
    const id = this.generateFileId(filePath);

    return filePath.replace(fileName, `${id}.${extension}`);
  }
}