##Example script
#Aim: merging/joining two dataframes (tables) based on a common column

#make dataframes
df1 <- data.frame(c('ARG','FRA', 'GBR', 'VNM'),c(100, 200, 300, 500),stringsAsFactors = FALSE)
names(df1)<- c("lkey","value")
df2 <- data.frame(c('ARG','FRA','VNM'),c("Argentina", "France", "Vietnam" ),c("Latin America", "Europe", "Asia Pacific" ),stringsAsFactors = FALSE)
names(df2)<- c("rkey","country","region")

#look at them
df1
df2

#join on the ISO3 columns - here they are called lkey and rkey for clarity
df_merged<- merge(df1,df2,by.x<-"lkey", by.y ="rkey",all = FALSE)

#check it worked 
df_merged
#for more info on merge function see here: https://stat.ethz.ch/R-manual/R-devel/library/base/html/merge.html

