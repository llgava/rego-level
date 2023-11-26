import re
import glob
import json

def remove_json_comments_from(content):
  """
    Remove every comment from a JSON file.

    See Also
    --------
    Original method from: https://github.com/Bedrock-OSS/regolith-filters/blob/c57989f3de3ac3bd34ac7464f131a007f51b12eb/json_cleaner/json_cleaner.py#L4
  """
  contents = ""
  for line in content.splitlines():
    cleanedLine = line.split("//", 1)[0]

    if len(cleanedLine) > 0 and line.endswith("\n") and "\n" not in cleanedLine:
        cleanedLine += "\n"

    contents += cleanedLine

  while "/*" in contents:
    preComment, postComment = contents.split("/*", 1)
    contents = preComment + postComment.split("*/", 1)[1]

  return json.loads(contents)

def remove_js_comments_from(content):
  """
    Remove every comment from a JS file.
  """

  content = re.sub(r'//.*', '', content)
  content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
  content_lines = [line.strip() for line in content.splitlines() if line.strip()]
  content = ''.join(content_lines)

  return content

def main():
  BP_FILES = glob.glob('BP/**/*.js', recursive=True) + glob.glob('BP/**/*.json', recursive=True)
  RP_FILES = glob.glob('RP/**/*.json', recursive=True)
  FILES = BP_FILES + RP_FILES

  for filePath in FILES:
    try:
      with open(filePath, "r", encoding="utf-8") as file:

        # JSON Files
        if (filePath.endswith('.json')):
          json_data = remove_json_comments_from(file.read())
        
          with open(filePath, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=2, ensure_ascii=False)
          continue

        # JS Files
        js_data = remove_js_comments_from(file.read())

        with open(filePath, "w", encoding="utf-8") as file:
          file.write(js_data)

    except Exception as e:
      print("Error in file: " + file)
      print(e)
      raise

if __name__ == '__main__':
  main()
