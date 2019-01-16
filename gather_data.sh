#!/bin/bash
WD=$(pwd)
home=/home/tyler/
error=/home/tyler/data_gathering/data_gathering_errors
printf "Gathering p0f data...\n"
# first argument here is where the .pcap files are coming from, it assumes /home/tyler/
python $WD/p0f/p0fer.py $home $WD/p0f/unzipped_data/ $WD/p0f/p0fdata/ 2> $error/p0fError.log
printf "P0f data gathered\n\n"
printf "Gathering and ordering asn data...\n"
python $WD/asnGeoData/getASN.py $WD/asnGeoData/asnData.asn $WD/p0f/p0fdata/ 2> $error/asnError.
printf "Asn data ordered\n\n"
printf "Getting full asn data now...\n"
netcat whois.cymru.com 43 < $WD/asnGeoData/asnData.asn | sort -n > $WD/asnGeoData/asnFinalData.asn
printf "Done! asnFinalData.asn now holds all unique asn data\n\n"
printf "Getting mult_ipv data...\n"

reader(){
printf "Enter the location of imaal_full:\n"
read loc
}

reader
while [[ -z "${loc// }" ]]
do
	echo Please enter the full path to imaal.full
	reader
done
python $WD/mult_ipv_data/getMultData.py $loc $WD/mult_ipv_data/ 2> $error/multError.log
printf "Compiled mult_ipv4.py and mult_ipv6.py data\n\n"

printf "All data is held inside their respective directories\n"

printf "\nWould you like to move resulting data files into the plotting datalib/ directory?(y/n)\n"
read var

case "$var" in
"y" | "yes")
	;;
*)
	printf "Goodbye!\n"
	exit
	;;
esac
cp $WD/asnGeoData/asnFinalData.asn $home/graphs/Plotting/datalib/
cp $WD/p0f/p0fdata/*.p0f $home/graphs/Plotting/datalib/
cp $WD/mult_ipv_data/*.ipv $home/graphs/Plotting/datalib/
echo Files moved!

