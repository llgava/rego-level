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
}