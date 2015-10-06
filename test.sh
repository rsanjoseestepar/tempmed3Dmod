caseLists = `ls -1 *BWH.nrrd | cut -d "_labelmap.nrrd" -f1`

shellThickness=20

for cc in $caseLists; do


unu 2op gte ${cc}.nrrd 1 -o tmp.nrrd
ComputeDistanceMap -l tmp.nrrd -m Maurer -d tmp-dm.nrrd -p

unu 3op in_cl 0 tmp-dm.nrrd $shellThickness -t ushort -o tmp-lm.nrrd

#GenerateModel -i tmp-lm.nrrd -l 1 -o ${cc}.vtk
/Applications/Slicer.app/Contents/lib/Slicer-4.4/cli-modules/ModelMaker tmp-lm.nrrd -l 1 -n ${cc}

#Computing model from raw
#GenerateModel -i tmp.nrrd -l 1 -o cip-raw.vtk
#/Applications/Slicer.app/Contents/lib/Slicer-4.4/cli-modules/ModelMaker tmp.nrrd -l 1 -n slicer-raw

#Compute a downsampled model for quicker displayed
unu resample -k cubic:1,0 -i tmp-dm.nrrd -s x0.5 x0.5 = -o tmp-dm-ds.nrrd
unu 3op in_cl 0 tmp-dm-ds.nrrd $shellThickness -t ushort -o tmp-lm-ds.nrrd

#GenerateModel -i tmp-lm-ds.nrrd -l 1 -o cip-ds.vtk
/Applications/Slicer.app/Contents/lib/Slicer-4.4/cli-modules/ModelMaker tmp-lm-ds.nrrd -l 1 -n ${cc}_downsampled

done