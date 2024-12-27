import { EnderChest } from "./EnderChest.js";
import { EnderChestUtils } from "./utils/EnderChestUtils.js";

export class EnderChestContent {
  /** @type {Map<string, any>} */
  static CONTENT = new Map();

  /** @type {string} */
  _id;

  /** @type {string} */
  filePath;

  /** @type {string} */
  encryptedFilePath;

  /** @type {Array<{ hash: string, original: string, encrypted: string }>} The content data. */
  data;

  constructor(filePath) {
    this._id = EnderChestUtils.generateFileId(filePath);
    this.filePath = filePath;
    this.encryptedFilePath = EnderChestUtils.encryptFilePath(filePath);

    this.data = [];

    EnderChestContent.CONTENT.set(this._id, this);
  }

  /**
   * 
   * @param {string} original 
   * @param {string} encrypted 
   */
  addDataValue(original, encrypted) {
    this.data.push({
      hash: EnderChest.encrypt(original),
      original,
      encrypted
    });
  }
}