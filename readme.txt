This is intended to take a directory of masks and a directory of raw images, both as TIFFs, within which the color value of bits in a mask image is a unique ID to be used for quantitation or analysis of values at the coorresponding positions in the raw tiffs. The masks will likely be the output of an Ilastik or CellProfiler cell tracking workflow.

It is written to be compatible with the Jython compiler and core Jython libraries shipped with ImageJ 1.53, both of which were specified by working conditions at the time of writing and have their benefits and drawbacks now. This served out purposes at the time. 

Since this was written, many alternatives have arisen  - many much like us by researchers asking similar questions (such as the one pointed out in https://forum.image.sc/t/measure-tracked-spot-intensities-in-mamut-or-ilastik/27893) whose primary difference is focus and abstraction depth, and some (such as https://forum.image.sc/t/measuring-fluorescence-intensity-of-individual-cells/69802) which are not only similar and written by those like us but also with greater influence and contributorships. 

We recommend using Ilastik as described in the first link above if you are now asking "what is the intensity of each cell at each time point", you are willing & able, you have a bit of time, and you are free to install software. If you are stuck in an environment limited to ImageJ, you don't have time, and want to simply point the scq script at your data (see the path to hardcode at the top level of scq) and get an output, then this is the right software for you. Be aware that you must also write into the script the maximum size of your cells.

scq_process_stack is the highest level function - processes inputs of tiff(s) in two sets (raw and mask)
ilastik_singlecell_quant aggregates a list of per-cell averages per image
get_intensity_per_cell aggregates a list of per-cell-intensity and takes their average
distinguish_children is a shell for the time being to potentially contain code that will be used to reassign individual cells to their own lineages after a division event. 
current assumption is that you don't have a significant number of dividing cells in the time course imaged.
