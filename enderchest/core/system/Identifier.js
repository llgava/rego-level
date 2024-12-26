import fs from 'fs';
import jsonpath from 'jsonpath';
import { EnderChest } from '../EnderChest.js';
import { EnderChestUtils } from '../utils/EnderChestUtils.js';
import { EnderChestContent } from '../EnderChestContent.js';

export class Identifier {
  static #PATHS = [
    "$..description.identifier",
    "$..value",
    '$..components["minecraft:block_placer"].block'
  ];

  encryptAndSave(filePath) {
    const rawData = fs.readFileSync(filePath, 'utf-8');
    const data = JSON.parse(rawData);

    for (const JSONPath of Identifier.#PATHS) {
      const id = jsonpath.query(data, JSONPath)[0];
      const hash = EnderChest.encrypt(id);
      
      const content = new EnderChestContent(id, hash, filePath);
      const aes = content.data.values.filter((obj) => obj.hash === hash)[0].encrypted;
      const value = `${aes.slice(0, 16)}:${aes.slice(16)}`;

      const path = jsonpath.paths(data, JSONPath)[0];
      jsonpath.apply(data, jsonpath.stringify(path), () => value);

      fs.writeFileSync(content.data.encryptedPath, JSON.stringify(data, null, 2));

      EnderChestContent.CONTENT.set(EnderChestUtils.generateFileId(filePath), content);
    }

    fs.unlinkSync(filePath);
  }
}