This is intended to take a directory of masks and a directory of raw images, both as TIFFs, within which the color value of bits in a mask image is a unique ID to be used for quantitation or analysis of values at the coorresponding positions in the raw tiffs. 

scq_process_stack is the highest level function - processes inputs of tiff(s) in two sets (raw and mask)
ilastik_singlecell_quant aggregates a list of per-cell averages per image
get_intensity_per_cell aggregates a list of per-cell-intensity and takes their average
distinguish_children is a shell for the time being to potentially contain code that will be used to reassign individual cells to their own lineages after a division event. 