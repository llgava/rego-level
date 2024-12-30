import fs from "fs";
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
   * @type {Array<{ hash: string, original: string, encrypted: string, type: string, line: number }>} The encrypted data array.
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
   * @param {any} type The content data type. Use "ContentTypes".
   */
  addDataValue(original, encrypted, type) {
    this.data.push({
      hash: EnderChest.encrypt(original),
      original,
      encrypted,
      type: type.toUpperCase() || 'UNDEFINED',
      line: this.#getEncryptedDataLine(original)
    });
  }

  #getEncryptedDataLine(original) {
    const rawData = fs.readFileSync(this.filePath, { encoding: "utf-8" });
    const lines = rawData.split('\n');

    for (const [i, line] of lines.entries()) {
      const code = i + 1;

      if (!line.includes(original)) continue;
      if (this.data.filter((content) => content.line === code).length > 0) continue;

      return code;
    }
  }

  /**
   * Get all or specific encrypted content.
   * @param {string|undefined} key The content key.
   * @returns {Map<string, EnderChestContent>} If a key is parsed, just one content will be returned.
   */
  static getContent(key = undefined) {
    return !key ? EnderChestContent.#CONTENT : EnderChestContent.#CONTENT.get(key);
  }

  static getParsedJSON() {
    return Object.fromEntries(this.getContent());
  }
}