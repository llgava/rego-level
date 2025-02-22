import { glob } from 'glob';
import { EnderChest } from "./EnderChest.js";
import { Logger } from "./utils/Logger.js";
import { Settings } from "./utils/Settings.js";
import { EnderChestContent } from './EnderChestContent.js';
import { VerySimpleScriptWrintingTextFile } from './web/VerySimpleScriptWrintingTextFile.js';

// ===================== NEED TO BE UPDATED ===================== 
Settings.ignore.push(
  "**/*/manifest.json",
  "**/*/languages.json"
);
// ==============================================================

function initialize() {
  if (!Settings.secretKey) {
    Logger.error('SOURCE CODE NOT ENCRYPTED >> The "secretKey" settings was not parsed in filter configuration.');
    return;
  }

  if (!Settings.isValidKeyBitsSize()) {
    Logger.error(`SOURCE CODE NOT ENCRYPTED >> The "keySize" value of ${Settings.keySize} is not valid. The options are 128, 192 or 256.`);
    return;
  }

  if (!Settings.isValidSecretKey()) {
    Logger.error(`SOURCE CODE NOT ENCRYPTED >> The length of "secretKey" should be ${Settings.keySize / 8} for ${Settings.keySize}-bits. The parsed length was ${Settings.secretKey.length}.`);
    return;
  }

  glob(["BP/**/*.json"], { ignore: Settings.ignore }).then((files) => {
    for (const file of files) {
      EnderChest.identifier.encryptAndSave(file);
    }

    VerySimpleScriptWrintingTextFile.buildWebView();
    VerySimpleScriptWrintingTextFile.buildTextFile();
  });
}

initialize();