from db import init_connection_new, init_connection_old



def fetch_clients():
    old_conn = init_connection_old()
    with old_conn.cursor() as cursor:
        cursor.execute("""
        SELECT ID, post_title, post_name
        FROM guia_posts
        WHERE post_title != post_name
        AND NOT post_name LIKE '%-v1'
        AND NOT post_name LIKE '%-2'
        AND NOT post_name LIKE '%-3'
        AND NOT post_name LIKE 'field_%'
        AND NOT post_name LIKE 'group_%'
        AND NOT post_title LIKE '::%';""")
        anunciantes = cursor.fetchall()
    old_conn.close()
    return anunciantes

def fetch_attributes(id):
    old_conn = init_connection_old()
    with old_conn.cursor() as cursor:
        cursor.execute("""
        SELECT meta_key, meta_value
        FROM guia_postmeta
        WHERE post_id = %s;""", id)
        attributes = cursor.fetchall()
    old_conn.close()
    return attributes


def insert_client(id, name, slug, activity, image, clasification, address, phone_1, phone_2, phone_3, page, maps, youtube, instagram, tiktok):
    new_conn = init_connection_new()
    with new_conn.cursor() as cursor:
        cursor.execute("""
        INSERT INTO ANUNCIANTES (ID, NAME, SLUG, ACTIVITY, IMAGE, CLASIFICATION, ADDRESS, PHONE_1, PHONE_2, PHONE_3, PAGE, MAPS, YOUTUBE, INSTAGRAM, TIKTOK) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (id, name, slug, activity, image, clasification, address, phone_1, phone_2, phone_3, page, maps, youtube, instagram, tiktok))
    new_conn.commit()
    new_conn.close()

def migrate_client(client):
    attributes = fetch_attributes(int(client['ID']))
    curr_client = {}

    curr_client['id'] = client['ID']

    if client['post_title'].startswith('• '): # Si empieza con "• "
        curr_client["name"] = client['post_title'].replace("• ", "") # Se le quita y se le agrega
    else:
        curr_client["name"] = client['post_title'] # Si no, se agrega el nombre normal
    
    curr_client["slug"] = client['post_name']

    for attr in attributes:
        if attr['meta_key'] == 'actividad':
            curr_client["activity"] = attr['meta_value']
        elif attr['meta_key'] == 'clasificacion':
            curr_client["clasification"] = attr['meta_value']
        elif attr['meta_key'] == 'direccion':
            curr_client['address'] = attr['meta_value']
        elif attr['meta_key'] == 'telefono':
            curr_client['phone_1'] = attr['meta_value']
        elif attr['meta_key'] == 'telefono_2':
            curr_client['phone_2'] = attr['meta_value']
        elif attr['meta_key'] == 'telefono_3':
            curr_client['phone_3'] = attr['meta_value']
        elif attr['meta_key'] == 'web_url':
            curr_client['page'] = attr['meta_value']
        elif attr['meta_key'] == 'google_map':
            curr_client['maps'] = attr['meta_value']
        elif attr['meta_key'] == 'youtube':
            curr_client['youtube'] = attr['meta_value']
        elif attr['meta_key'] == 'instagram':
            curr_client['instagram'] = attr['meta_value']



    if "activity" not in curr_client:
        curr_client['activity'] = ''
    
    if "clasification" not in curr_client:
        curr_client['clasification'] = 'PE'

    if "address" not in curr_client:
        curr_client['address'] = ''

    if "phone_1" not in curr_client:
        curr_client['phone_1'] = ''
    if "phone_2" not in curr_client:
        curr_client['phone_2'] = ''
    if "phone_3" not in curr_client:
        curr_client['phone_3'] = ''
    
    if "page" not in curr_client:
        curr_client['page'] = ''

    if "maps" not in curr_client:
        curr_client['maps'] = ''

    if "youtube" not in curr_client:
        curr_client['youtube'] = ''

    if "instagram" not in curr_client:
        curr_client['instagram'] = ''

    curr_client['tiktok'] = ''
    curr_client['image'] = b''

    insert_client(
        curr_client['id'],
        curr_client['name'],
        curr_client['slug'],
        curr_client['activity'],
        curr_client['image'],
        curr_client['clasification'],
        curr_client['address'],
        curr_client['phone_1'],
        curr_client['phone_2'],
        curr_client['phone_3'],
        curr_client['page'],
        curr_client['maps'],
        curr_client['youtube'],
        curr_client['instagram'],
        curr_client['tiktok'],
    )


clients = fetch_clients()
for client in clients:
    migrate_client(client)

    