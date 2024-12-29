import fs from 'fs';
import jsonpath from 'jsonpath';
import { EnderChest } from '../EnderChest.js';
import { EnderChestContent } from '../EnderChestContent.js';
import { ContentTypes } from './ContentType.js';

export class Identifier {
  static REGEX = /^(?!minecraft:)[a-zA-Z0-9_]+:[a-zA-Z0-9_]+$/;

  static #PATHS = [
    "$..description.identifier",

    // Behavior Pack Items
    '$..components["minecraft:entity_placer"].entity',
    '$..components["minecraft:block_placer"].block'
  ];

  encryptAndSave(filePath) {
    const rawData = fs.readFileSync(filePath, 'utf-8');
    const data = JSON.parse(rawData);
    
    const content = new EnderChestContent(filePath);
    
    for (const JSONPath of Identifier.#PATHS) {
      const identifier = jsonpath.query(data, JSONPath)[0];

      if (!identifier) {
        fs.writeFileSync(content.encryptedFilePath, JSON.stringify(data, null, 2));
        continue;
      };

      const hash = EnderChest.encrypt(identifier);
      const truncatedHash = hash.substring(0, 32); // Limits to 32 characters for big hashs.

      const encrypted = `${truncatedHash.slice(0, 16)}:${truncatedHash.slice(16)}`;
      const path = jsonpath.paths(data, JSONPath)[0];

      if (Identifier.isValidIdentifier(identifier)) {
        content.addDataValue(identifier, encrypted, ContentTypes.IDENTIFIER);
        jsonpath.apply(data, jsonpath.stringify(path), () => encrypted);
      }

      fs.writeFileSync(content.encryptedFilePath, JSON.stringify(data, null, 2));
    }

    fs.unlinkSync(filePath);
  }

  static isValidIdentifier(value) {
    return Identifier.REGEX.test(value);
  }
}