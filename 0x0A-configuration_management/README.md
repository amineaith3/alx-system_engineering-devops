# Configuration management

In this project, I started working with Puppet as a configuration management tool.
I practiced writng Puppet manifest files to create a file, install a package, end execute a command.

## Taks :page_with_curl:
* **0. Create a file**
	* [0-create_a_file.pp](./0-create_a_file.pp): Puppet manifest file that creates a file`school` in the `/tmp`directory.
	* File permission:`0744`.
	* File group: `www-data`.
	* File owner: `www-data`.
	* File content : `I love Puppet`.
