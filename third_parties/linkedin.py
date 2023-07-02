import os
import requests


def scrape_linkedin_profile(linkedin_profile_url: str):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""
    api_endpoint = "https://gist.githubusercontent.com/parahall/d305f52ddbb94ff5196b0cb9aa067f83/raw/a8256d0b17419017535e13af3953ac6332ec82fd/yoni-levin.json"
    # header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
    # params = {"url": linkedin_profile_url}
    # response = requests.get(api_endpoint, params=params, headers=header_dic)
    response = requests.get(api_endpoint)
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k
        not in [
            "groups",
            "activities",
            "first_name",
            "last_name",
            "country",
            "people_also_viewed",
            "certifications",
            "profile_pic_url",
            "public_identifier",
            "background_cover_image_url",
            "state",
            "accomplishment_courses",
            "volunteer_work",
            "recommendations",
        ]
    }
    data = remove_links(data)

    print("Scrapped finished")
    return data


def remove_links(obj):
    if isinstance(obj, dict):
        # For dictionaries, create a new dictionary with only the key-values that are not URLs
        new_obj = {}
        for key, value in obj.items():
            # Recursively call remove_links on the value
            new_value = remove_links(value)
            # Check if the value is a URL, in this example if it is a string and starts with 'http' it is assumed to
            # be a URL
            if not (isinstance(new_value, str) and new_value.startswith("http")):
                new_obj[key] = new_value
        return new_obj
    elif isinstance(obj, list):
        # For lists, create a new list with the elements after recursively calling remove_links
        return [remove_links(item) for item in obj]
    else:
        # If the object is not a dictionary or a list, return it as is
        return obj
