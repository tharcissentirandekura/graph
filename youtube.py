from googleapiclient.discovery import build
import sys

def search_singer_actions(singer_name, api_key):
    """
    Searches for a singer's actions on YouTube based on their name.

    Args:
        singer_name (str): The name of the singer to search for.
        api_key (str): The YouTube API key.

    Returns:
        list: A list of dictionaries containing video ID, title, views, and publication year.
    """
    youtube = build("youtube", "v3", developerKey=api_key)

    try:
        # Search for the singer's name on YouTube
        search_response = youtube.search().list(
            q=singer_name,
            type="video",
            part="id,snippet",
            maxResults=10
        ).execute()

        # Retrieve video details
        video_details = []
        for item in search_response["items"]:
            video_id = item["id"]["videoId"]
            video_response = youtube.videos().list(
                part="statistics,snippet",
                id=video_id
            ).execute()
            video_details.append({
                "video_id": video_id,
                "title": video_response["items"][0]["snippet"]["title"],
                "views": int(video_response["items"][0]["statistics"]["viewCount"]),
                "publication_year": int(video_response["items"][0]["snippet"]["publishedAt"][:4])
            })

        return video_details
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage
singer_name = sys.argv[1]
api_key = "AIzaSyC2LLNvNS397Jduz5g08TtnvBNDpusiIw0"
video_details = search_singer_actions(singer_name, api_key)

for video in video_details:
    print(f"Video ID: {video['video_id']}")
    print(f"Title: {video['title']}")
    print(f"Views: {video['views']}")
    print(f"Publication Year: {video['publication_year']}")
    print()
