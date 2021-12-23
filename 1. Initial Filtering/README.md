# Initial Filtering

The goal in the first part is getting the important hashtags from both twitter and instagram data. To do that, we need to pick important keywords to as the first layer of filter to the post_captions and post_content column in the instagram and twitter data respectively. Then, we select the hashtags that appears the most frequently out of all the available ones. Afterwards, we store those hashtags in two other external files, one containing instagram hashtags and the other containing twitter hashtags.

There are three main files in this folder. EventData_InitFiltering.ipynb, contains the lines of code required to achieve the important hashtags. ig_important_hashtags.txt and tw_important_hashtags.txt contains the collected important hashtags for easier viewing.
