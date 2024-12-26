import path from 'path';
import { EnderChestUtils } from "./utils/EnderChestUtils.js";

export class EnderChestContent {
  static CONTENT = new Map();
  _id; data;

  constructor(original, hash, filePath) {
    const fileName = path.basename(filePath);
    this._id = EnderChestUtils.generateFileId(filePath);

    if (EnderChestContent.CONTENT.has(this._id)) {
      this.data = EnderChestContent.CONTENT.get(this._id).data;
      this.data.values.push({ hash, original, encrypted: hash.substring(0, 32) });
      return;
    }

    this.data = {
      filePath,
      encryptedPath: filePath.replace(fileName, `${this._id}.json`),
      values: [{ hash, original, encrypted: hash.substring(0, 32) }]
    };
  }
}