[Dataset Excel Preview Link](https://feutecheduph-my.sharepoint.com/:x:/g/personal/201620164_fit_edu_ph/EVQfIvSx1HtBoj79gzGXS3QBsvSQZ2U1MFaKlegc8tcECw?e=pL2gQa)<br>
[Development Files](https://drive.google.com/drive/folders/1N9nUCiFK_KFisjDLVOITIKK2bQrXjDUt?usp=sharing)<br>
[PH GeoJSON Link](https://gadm.org/download_country.html)<br>

raw_dataset.csv  
↓  
province_region_dates.csv  
(extracted province, region, and July 20–25 columns from raw_dataset)  
↓  
province_region_dates_reformatted.csv  
(reformatted columns to: province, region, Jul-20, Jul-21, Jul-22, Jul-23, Jul-24, Jul-25)  
↓  
province-data.csv  
(removed whitespace from province names, e.g., "Davao DelSur" → "DavaoDelSur")  
↓  
province-data-combined.csv  
(merged data with the same province name, e.g., "Abra" + "Abra")  
↓  
province-data-combined-convert.csv  
(added missing data for July 25)  
↓  
renamed province-data-combined-convert2 to province-data  
(renamed for system compatibility with GeoJSON)
