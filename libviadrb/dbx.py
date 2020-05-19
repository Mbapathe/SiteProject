import dropbox

key = 'sJFn4RS2vJ0AAAAAAAAkPxEJqXCDK3ThZxY6-Oi1J2b_kdqoS04B4x5_N868I-Mo'

def drb_con():
    try:
        dbx=dropbox.Dropbox(key)
    except:
        dbx='connection problems'
    return dbx



#for entry in dbx.files_list_folder('').entries:
#    print(entry.name)
# dbx.users_get_current_account()