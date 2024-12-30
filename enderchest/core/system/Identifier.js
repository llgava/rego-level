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
    '$["minecraft:item"]..["minecraft:entity_placer"].entity',
    '$..["minecraft:block_placer"].block'
  ];

  encryptAndSave(filePath) {
    const rawData = fs.readFileSync(filePath, 'utf-8');
    const data = JSON.parse(rawData);
    
    const content = new EnderChestContent(filePath);
    
    for (const JSONPath of Identifier.#PATHS) {
      const identifiers = jsonpath.query(data, JSONPath);

      if (identifiers.length === 0) {
        fs.writeFileSync(content.encryptedFilePath, JSON.stringify(data, null, 2));
        continue;
      };

      for (const identifier of identifiers) {
        const i = identifiers.indexOf(identifier);
        const hash = EnderChest.encrypt(identifier);
  
        const encrypted = `${hash.slice(0, 16)}:${hash.slice(-16)}`;
        const path = jsonpath.paths(data, JSONPath)[i];

        if (Identifier.isValidIdentifier(identifier)) {
          content.addDataValue(identifier, encrypted, ContentTypes.IDENTIFIER);
          jsonpath.apply(data, jsonpath.stringify(path), () => encrypted);
        }
      }

      fs.writeFileSync(content.encryptedFilePath, JSON.stringify(data, null, 2));
    }

    fs.unlinkSync(filePath);
  }

  static isValidIdentifier(value) {
    return Identifier.REGEX.test(value);
  }
}