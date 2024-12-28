import fs from 'fs';
import path from 'path';
import Handlebars from 'handlebars';
import { EnderChestContent } from "../EnderChestContent.js";
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export class VerySimpleScriptWrintingTextFile {

  static buildWebView() {
    const templateHTMLPath = path.join(__dirname, 'index.html');
    const outputPath = path.join('BP/', 'ender_chest_content.html');

    const contents = Array.from(EnderChestContent.getContent().values()).map(content => ({
      id: content._id,
      fullFilePath: content.filePath,
      filePath: path.basename(content.filePath),
      encryptedFilePath: path.basename(content.encryptedFilePath),
      dataSize: content.data.length,
      data: content.data
    }));
 
    // Template Handlebars
    const template = fs.readFileSync(templateHTMLPath, { encoding: 'utf-8' });
    
    const compiled = Handlebars.compile(template);
    const html = compiled({ contents });
    
    fs.writeFileSync(outputPath, html);
  }

  static buildTextFile() {
    let content = '';
    const filePath = path.join('BP/', 'future_webview.txt');

    for (const [key, value] of EnderChestContent.getContent()) {
      content += `[${key}] - ${value.encryptedFilePath} -> ${value.filePath}\n`;
      
      if (value.data.length > 0) {
        content += '              Encrypted data:\n';
        for (const data of value.data) {
          content += `                  - ${data.encrypted} -> ${data.original}\n`;
        }
      }
    }

    fs.writeFileSync(filePath, content, { encoding: 'utf-8' });
  }
}