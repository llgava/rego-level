import { EnderChest } from "./EnderChest.js";
import { EnderChestUtils } from "./utils/EnderChestUtils.js";

export class EnderChestContent {
  /** @type {Map<string, EnderChestContent>} */
  static #CONTENT = new Map();

  /** @type {string} The file path ID. */
  _id;

  /** @type {string} The original file path. */
  filePath;

  /** @type {string} The encrypted file path. */
  encryptedFilePath;

  /**
   * @type {Array<{ hash: string, original: string, encrypted: string }>} The encrypted data array.
   * */
  data;

  constructor(filePath) {
    this._id = EnderChestUtils.generateFileId(filePath);
    this.filePath = filePath;
    this.encryptedFilePath = EnderChestUtils.encryptFilePath(filePath);

    this.data = [];

    EnderChestContent.#CONTENT.set(this._id, this);
  }

  /**
   * Adds new encrypted data to this content.
   * @param {string} original The original content value.
   * @param {string} encrypted The encrypted content value.
   */
  addDataValue(original, encrypted) {
    this.data.push({
      hash: EnderChest.encrypt(original),
      original,
      encrypted
    });
  }

  /**
   * Get all or specific encrypted content.
   * @param {string|undefined} key The content key.
   * @returns {Map<string, EnderChestContent>} If a key is parsed, just one content will be returned.
   */
  static getContent(key = undefined) {
    return !key ? EnderChestContent.#CONTENT : EnderChestContent.#CONTENT.get(key);
  }
}