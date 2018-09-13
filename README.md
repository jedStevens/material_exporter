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
	- is named one of: `['alb', 'ao', 'mtl', 'rgh', 'emi']`


The `.kra` file provided contains layer-groups with these names as well as a default black background.

Note that this exporter only exports layers with the names used in the `.kra` file. This is for use in a PBR renderer but you can toggle specific maps off if you like by removing the layer group. For example if your model has no emission map needed, just remove the `emi` layer group to ignore it.

### Installing
Put the `material_exporter` and the `material_exporter.desktop`folder in the Krita resources folder.

On Linux this folder is `~/.local/share/krita/pykrita/`

### Enabling
Navigating to `Settings > Configure Krita`.

Go to the `Python Plugin Manager`.

Scroll to `Material Exporter` and ensure it is checked.

If you cannot see the docker, navigate to `Settings > Docker > Material Exporter` and click the checkbox.


### Exporting
There are 3 fields to fill in.


1. Base Path
Point to the project folder you are working in.

2. Model
A name of an existing folder within the base path. The Material Exporter does not create folders that do not exist in hopes of keeping cleaner projects.

3. Material
A name of the material you are working. Once again you are required to create the folder initially.
