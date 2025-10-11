# DownloadsSorter

A Python utility that automatically organizes files in your Downloads folder by moving them into categorized subdirectories based on their file extensions. Perfect for keeping your Downloads folder clean and organized on macOS and Unix-based systems.

## Features

- **Automatic File Organization**: Sorts files into predefined categories based on file extensions
- **Directory Creation**: Automatically creates necessary directories if they don't exist
- **Cross-Platform Support**: Works on macOS and Unix-based systems
- **Windows File Handling**: Specifically handles Windows executables and installers
- **Safe File Operations**: Validates file moves before deleting originals
- **Developer Mode**: Optional testing mode for safe development

## ToDo List
- [ ] Separate out the types into separate config file
- [ ] Add a way to update the config file from the command call
- [ ] Add flags to allow for dry-run

## Requirements

- Python 3.6 or higher
- macOS or Unix-based operating system
- Standard Python libraries (no external dependencies required)

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. No additional installation required - uses only Python standard library

## Usage

### Basic Usage

```bash
python SortDownloads.py
```

The script will automatically:
1. Check your `~/Downloads` directory
2. Create necessary subdirectories if they don't exist
3. Move files to appropriate categories based on their extensions
4. Validate successful moves before deleting original files

### Developer Mode

To enable testing mode (creates a `TESTING` subdirectory in Downloads):

1. Edit `SortDownloads.py`
2. Change `DEVELOPER_BUILD = False` to `DEVELOPER_BUILD = True`
3. Run the script

## File Categories

The script organizes files into the following categories:

| Category | File Extensions | Description |
|----------|----------------|-------------|
| **Documents** | pdf, doc, docx, pages, numbers | Office documents and PDFs |
| **Text_Files** | txt, csv, json, md | Plain text and data files |
| **Software** | dmg, pkg | macOS software packages |
| **Images** | cr2, png, jpg, jpeg | Image files |
| **Videos** | mp4, mpg, mpeg | Video files |
| **Disk_Images** | iso | Disk image files |
| **Subtitles** | srt | Subtitle files |
| **Archives** | zip, tar, gz | Compressed archives |
| **Windows_Junk** | exe, msi | Windows executables and installers |

## Configuration

### Adding New File Types

To add support for new file types, edit the extension lists in `SortDownloads.py`:

```python
documentTypes = ["pdf", "doc", "docx", "pages", "numbers", "xlsx"]  # Add xlsx
imageTypes = ["cr2", "png", "jpg", "jpeg", "gif", "svg"]  # Add gif, svg
```

### Creating New Categories

To add a new category:

1. Create a new extension list:
```python
audioTypes = ["mp3", "wav", "flac", "aac"]
```

2. Add it to the `directoriesDict`:
```python
directoriesDict = {
    "Documents": documentTypes,
    "Text_Files": flatDocumentTypes,
    "Software": softwareTypes,
    "Disk_Images": diskImageTypes,
    "Images": imageTypes,
    "Videos": videoTypes,
    "Subtitles": subtitleType,
    "Archives": archiveType,
    "Windows_Junk": windowsTypes,
    "Audio": audioTypes,  # Add new category
}
```

## Safety Features

- **File Validation**: The script validates that files are successfully copied before deleting originals
- **Error Handling**: Graceful handling of file operation errors
- **Developer Mode**: Safe testing environment that doesn't affect your main Downloads folder
- **Directory Detection**: Skips directories and only processes files

## Exit Codes

- `0`: Success
- `1`: General error
- `2`: Directory not found

## License

This project is open source. Feel free to modify and distribute as needed.

## Version History

- **v1.0**: Initial release with basic file sorting functionality