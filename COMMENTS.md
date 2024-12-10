### How to run
In order to run the script, navigate to the `slcsp` directory from a terminal window. When you are in the directory, run the following command:

```
python get_slcsp.csv
```

The python script will create a backup of `slcsp.csv` called `slcsp_backup.csv` and update `slcsp.csv` to contain the second lowest Silver Plan rates for the zip codes in the file. The script will also output each line that will get written to the new csv file.

If you would like to rerun the script, ensure that you delete the new `slcsp.csv` file and rename `slcsp_backup.csv` to `slcsp.csv`. To do so, you can run the following commands in the same terminal window:

```
rm slcsp.csv
mv slcsp_backup.csv slcsp.csv
```
