# Material Exporter
## Brief
Thank you for downloading Mr. Jed's Material Exporter. This docker is
intended to help Krita users export many layers at a time into a
specific folder structure to help organizing materials.
-- Mr Jed

## How To
### Basics
This plugin intends to be working with the corresponding `.kra` that
has been provided with this repository.


It exports the first level layer groups that have:
	- at least one child layer
	- is named one of: ['alb', 'ao', 'mtl', 'rgh', 'emi']


	The `.kra` file provided contains layer-groups with these names as well
	as a default black background.

### Installing The Plugin
Put the `material_exporter` and the `material_exporter.desktop`folder in the Krita resources folder.
`~/.local/share/krita/pykrita/`

Your Krita folder should look like this:
    ~/.local/share/krita/pykrita/material_exporter
                                /material_exporter.desktop

###  Exporting
There are 3 fields to fill in.


1. Base Path
Point to the project folder you are working in.

2. Model
A name of an existing folder within the base path. The Material Exporter does not create folders that do not exist in hopes of keeping cleaner projects.

3. Material
A name of the material you are working. Once again you are required to create the folder initially.
