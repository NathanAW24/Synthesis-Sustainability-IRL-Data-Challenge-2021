import pandas as pd
import pyodbc
import configparser


def importing_tw_event_data():
    config = configparser.ConfigParser()
    config.read('Sustainability_Config.ini')

    # DB Settings
    driver = config['database']['driver']
    server = config['database']['server']
    database = config['database']['database']
    conn_str = 'DRIVER='+driver+'; SERVER='+server+'; DATABASE='+database

    # Accessing DB
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT [post_content],[post_is_retweet],[post_is_truncated],[post_like_count],
        [post_retweet_count],[post_media],[post_hashtags],[post_reply_to_post_id],[segment_name]
        FROM [Sustainability_Challenge_DB].[dbo].[Event_Data_TW]
        WHERE [post_hashtags] LIKE '%surplusfood%'
        OR [post_hashtags] LIKE '%Courtauld2025%'
        OR [post_hashtags] LIKE '%christmasleftovers%'
        OR [post_hashtags] LIKE '%plantbased%'
        --ORDER BY [post_like_count] DESC
        ORDER BY cast([post_retweet_count] as int) DESC
        """)

    fields = [i[0] for i in cursor.description]  # extracts column headers
    db_tw_event_data = [dict(zip(fields, rowindb))
                        for rowindb in cursor.fetchall()]
    # Zip function maps each column value to their respective rows => output is a tuple which is converted into a dictionary of tuples
    # cursor.fetchall() => returns list of tuples

    df_tw_event_data = pd.DataFrame(db_tw_event_data)
    return df_tw_event_data  # By EDA on SQL, there is already less than 100 returned here


def importing_ig_event_data():
    config = configparser.ConfigParser()
    config.read('Sustainability_Config.ini')

    # DB Settings
    driver = config['database']['driver']
    server = config['database']['server']
    database = config['database']['database']
    conn_str = 'DRIVER='+driver+'; SERVER='+server+'; DATABASE='+database

    # Accessing DB
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    cursor.execute("""SELECT [post_type],[post_caption],[post_hashtags],[post_comments],[post_likes],[segment_name] 
    FROM [Sustainability_Challenge_DB].[dbo].[Event_Data_IG] 
    WHERE [post_hashtags] LIKE '%#sgfood%' 
    OR [post_hashtags] LIKE '%#sustainable%' 
    OR [post_hashtags] LIKE '%#sgfoodies%' 
    OR [post_hashtags] LIKE '%#singaporefood%' 
    OR [post_hashtags] LIKE '%#goodfoodpeoplesg%' 
    OR [post_hashtags] LIKE '%#vegan%' 
    OR [post_hashtags] LIKE '%#meatless%' 
    OR [post_hashtags] LIKE '%#plantbasedfoods%' 
    OR [post_hashtags] LIKE '%#eatwideawake%' 
    OR [post_hashtags] LIKE '%#homecoking%' 
    OR [post_hashtags] LIKE '%#cookingmadeeasy%' 
    OR [post_hashtags] LIKE '%#plantbaseddiet%' 
    OR [post_hashtags] LIKE '%#igsgfoodies%' 
    OR [post_hashtags] LIKE '%#goodfoodpeople%' 
    OR [post_hashtags] LIKE '%#vegetarian%' 
    OR [post_hashtags] LIKE '%#sustainability%' 
    OR [post_hashtags] LIKE '%#crustsingapore%' 
    OR [post_hashtags] LIKE '%#goodpeople%' 
    OR [post_hashtags] LIKE '%#upcycle%' 
    OR [post_hashtags] LIKE '%#foodphotography%' 
    ORDER BY [post_likes] DESC""")

    # SELECT TOP 2 [user_id],[user_name],[post_id],[post_shortcode],[post_type],[post_date],[post_caption],[post_tagged_users],[post_hashtags],[post_mentions],[post_comments],[post_likes],[segment_name] FROM[Sustainability_Challenge_DB].[dbo].[Event_Data_IG]

    fields = [i[0] for i in cursor.description]  # extracts column headers
    db_ig_event_data = [dict(zip(fields, rowindb))
                        for rowindb in cursor.fetchall()]
    # Zip function maps each column value to their respective rows => output is a tuple which is converted into a dictionary of tuples
    # cursor.fetchall() => returns list of tuples

    df_ig_event_data = pd.DataFrame(db_ig_event_data)  # Converts to dataframe
    top100_rows_post_likes = df_ig_event_data[df_ig_event_data.post_likes > 350]
    return top100_rows_post_likes  # returns top rows
