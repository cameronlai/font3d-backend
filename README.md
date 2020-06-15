# font3d Backend

font3d is a web app built to generate 3D Text STL files. It utilizes OpenSCAD as the drawing tool.

## Deply Instructions

### Build Container Image

gcloud builds submit --tag gcr.io/personal-279606/font3d

### Deploy to Google Cloud Run

gcloud run deploy --image gcr.io/personal-279606/font3d --platform managed

## Dependencies

- OpenSCAD

## License

The app is released under the MIT License and more information can be found in the LICENSE file.

## Contributions

font3d is a project to create some interesting font types that uses 3D dimension, breaking through the conventional 2D font types. All code is written in Open SCAD and can be printed out with a 3D printer.

Contributions for new font types and bug fixes are sincerely welcome!

## Available font types

- Basic - Basic font type drawn in Open SCAD

