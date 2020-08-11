#!/usr/bin/python
# -*- coding:utf-8 -*-

# Assignment 2
# Before working on this assignment please read these instructions fully. In the submission area,
# you will notice that you can click the link to Preview the Grading for each step of the assignment.
# This is the criteria that will be used for peer grading. Please familiarize yourself with
# the criteria before beginning the assignment.
#
# An NOAA dataset has been stored in the file
# 数据源
# "data/C2A2_data/BinnedCsvs_d100/4e86d2106d0566c6ad9843d882e72791333b08be3d647dcae4f4b110.csv".
# The data for this assignment comes from a subset of
# The National Centers for Environmental Information (NCEI) Daily Global Historical Climatology Network (GHCN-Daily).
# The GHCN-Daily is comprised of daily climate records from thousands of land surface stations across the globe.
#
# 数据来源, 和该作业的要求无关
# The data you have been given is near Singapore, Central Singapore Community Development Council,
# Singapore, and the stations the data comes from are shown on the map below.
# 准备: pip install mplleaflet
import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd


def leaflet_plot_stations(binsize, hashid):
    df = pd.read_csv('./data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    plt.figure(figsize=(8, 8))

    plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    # 在IDE里面触发显示, 如果在ipynb里面不需要这句
    mplleaflet.show()
    return mplleaflet.display()


leaflet_plot_stations(100, '4e86d2106d0566c6ad9843d882e72791333b08be3d647dcae4f4b110')
