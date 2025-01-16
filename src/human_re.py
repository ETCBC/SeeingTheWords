import analyzeppl
import data_frame_helper
def get_response(url):
    return analyzeppl.call_cameralyze(url)
def human_recon(image_data, prompt):
    data = data_frame_helper.get_data(prompt)

    print(data.head)
    failed_report = []
    for image in image_data:
        image_url = image['url']
        if  not check_duplicate(image_url, data):
            image_response = get_response(image['url'])

            if image_response['status'] == 200:
                response_data = human_response(image_response, image['url'])

                data.loc[len(data)] = response_data

            else:
                failed_report.append(image_response)

    return data, failed_report


def human_response(response, path):
    male = 0
    female = 0
    group_a = 0
    group_b = 0
    group_c = 0

    for data in response['data']['detections']:
         if data['gender']['gender'] == 'Male': male+=1
         else :female += 1

         min_age = data['age']['minimum']
         max_age = data['age']['maximum']
         if min_age < 12:
                group_a += 1
         elif min_age < 50:
                 group_b += 1
         elif min_age > 50:
                 group_c += 1

    return {'image_id': path, 'number': len(response['data']),
            'male': male, 'female': female, "age_group_a": group_a,
            'age_group_b':group_b, 'age_group_c': group_c, 'json_response': response}

def check_duplicate(url, df):
    return url in df['image_id']
