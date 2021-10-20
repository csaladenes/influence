import lzma,json,gzip
import urllib.request

remote_path='http://parltrack.euwiki.org/dumps/'
local_path='ep/'
save_path='ep/export/json/'

def load_file(file_name,saved=False):
    url=remote_path+file_name
    local_url=local_path+file_name
    if saved:
        try:
            print('downloading '+file_name+'...')
            urllib.request.urlretrieve(url, local_url)
        except:
            'file not found...'
    f=lzma.open(local_url)
    print('loading '+file_name+'...')
    return json.loads(f.read())

def save_local(eu_vt,path):
    json_str = json.dumps(eu_vt) + "\n"               # 2. string (i.e. JSON)
    json_bytes = json_str.encode('utf-8')            # 3. bytes (i.e. UTF-8)
    with gzip.GzipFile(save_path+path+".json.gz", 'w') as fout:   # 4. gzip
        fout.write(json_bytes)  
    return
  
def load_local(path):
    with gzip.GzipFile(save_path+path+".json.gz", 'r') as fin:    # 4. gzip
        json_bytes = fin.read()                      # 3. bytes (i.e. UTF-8)
    json_str = json_bytes.decode('utf-8')            # 2. string (i.e. JSON)
    return json.loads(json_str)  

def hu_country(c):
    hu_countries={'Hungary':'Magyarország','Romania':'Románia'}
    if c in hu_countries: return hu_countries[c]
    else: return c
    
def country_normalizer(country):
    sign='🇪🇺'
    if country=='Hungary': sign='🇭🇺'
    elif country=='Germany': sign='🇩🇪'
    elif country=='Belgium': sign='🇧🇪'
    elif country=='France': sign='🇫🇷'
    elif country=='Poland': sign='🇵🇱'
    elif country=='Italy': sign='🇮🇹'
    return country+' '+sign
    
def party_normalizer(party):
    if party in ['ALDE','ELDR']: return 'ALDE'
    elif party in ['ITS','ENF']: return 'ENF'
    elif party in ['NA','NI',['NA', 'NI'],'-','Independent']: return 'N/A'
    elif party in ['PPE','PPE-DE']: return  'EPP'
    elif party in ['Verts/ALE']: return  'Greens'
    elif party in ['S&D','PSE']: return 'S&D'
    elif party in ['ALDE Romania','Partidul Conservator','Partidul Puterii Umaniste']: return 'ALDE RO'
    elif party in ['Demokratikus Koalíció']: return 'DK'
    elif party in ['Együtt 2014 - Párbeszéd Magyarországért']:return 'Együtt PM'
    elif party in ['Fidesz-Magyar Polgári Szövetség',
        'Fidesz-Magyar Polgári Szövetség-Keresztény Demokrata Néppárt',
        'Fidesz-Magyar Polgári Szövetség-Kereszténydemokrata Néppárt',
        'Kereszténydemokrata Néppárt']:return 'FIDESZ-KDNP'
    elif party in ['Forumul Democrat al Germanitor din România']: return 'FDGR'
    elif party in ['Jobbik Magyarországért Mozgalom']:return 'Jobbik'
    elif party in ['Lehet Más A Politika']:return 'LMP'
    elif party in ['Magyar Demokrata Fórum','Modern Magyarország Mozgalom',
                'Szabad Demokraták Szövetsége']: return 'Egyéb'
    elif party in ['Magyar Szocialista Párt']: return 'MSZP'
    elif party in ['Partidul Democrat','Partidul Democrat-Liberal','Partidul Naţional Liberal',
        'Partidul Liberal Democrat','PNL']: return'PNL'
    elif party in ['Partidul Mișcarea Populară']: return 'PMP'
    elif party in ['Partidul Naţional Ţaranesc Creştin Democrat']:return 'PNȚCD'
    elif party in ['Partidul România Mare']:return 'PRM'
    elif party in ['PSD','Partidul Social Democrat','Partidul Social Democrat + Partidul Conservator']:return 'PSD'
    elif party in ['Romániai Magyar Demokrata Szövetség',
        'Uniunea Democrată Maghiară din România']:return 'RMDSZ'
    elif party in ['Uniunea Națională pentru Progresul României']: return 'UNPR'
    else: return party
    
def party_normalizer2(party):
    if party in ['ALDE','ELDR']: return 'ALDE ⏩'
    elif party in ['ITS','ENF']: return 'ENF 🌐'
    elif party in ['N/A','NA','NI',['NA', 'NI'],'-','Independent']: return 'N/A 👤'
    elif party in ['EPP','PPE','PPE-DE']: return  'EPP ⭐️'
    elif party in ['Greens','Verts/ALE']: return  'Greens 🌻'
    elif party in ['S&D','PSE']: return 'S&D 🔴'
    elif party in ['ECR']: return 'ECR 🦁'
    elif party in ['ALDE RO','ALDE Romania','Partidul Conservator','Partidul Puterii Umaniste']: return 'ALDE RO 🕊️'
    elif party in ['DK','Demokratikus Koalíció']: return 'DK 🔵'
    elif party in ['Együtt PM','Együtt 2014 - Párbeszéd Magyarországért']:return 'Együtt PM ✳️'
    elif party in ['Fidesz-Magyar Polgári Szövetség',
        'Fidesz-Magyar Polgári Szövetség-Keresztény Demokrata Néppárt',
        'Fidesz-Magyar Polgári Szövetség-Kereszténydemokrata Néppárt',
        'Kereszténydemokrata Néppárt','FIDESZ-KDNP']:return 'FIDESZ-KDNP 🍊'
    elif party in ['Forumul Democrat al Germanitor din România','FDGR']: return 'FDGR ⚫️'
    elif party in ['Jobbik Magyarországért Mozgalom','Jobbik']:return 'Jobbik ✅'
    elif party in ['Lehet Más A Politika','LMP']:return 'LMP 🏃‍♂️'
    elif party in ['Magyar Demokrata Fórum','Modern Magyarország Mozgalom',
                'Szabad Demokraták Szövetsége','Egyéb']: return 'Egyéb ⭕️'
    elif party in ['Magyar Szocialista Párt','MSZP']: return 'MSZP 🌸'
    elif party in ['Partidul Democrat','Partidul Democrat-Liberal','Partidul Naţional Liberal',
        'Partidul Liberal Democrat','PNL']: return'PNL 🔶'
    elif party in ['Partidul Mișcarea Populară','PMP']: return 'PMP 🍏'
    elif party in ['Partidul Naţional Ţaranesc Creştin Democrat','PNȚCD']:return 'PNȚCD ✳️'
    elif party in ['Partidul România Mare','PRM']:return 'PRM 🔱'
    elif party in ['PSD','Partidul Social Democrat','Partidul Social Democrat + Partidul Conservator']:return 'PSD 🌹'
    elif party in ['Romániai Magyar Demokrata Szövetség',
        'Uniunea Democrată Maghiară din România','RMDSZ']:return 'RMDSZ 🌷'
    elif party in ['Uniunea Națională pentru Progresul României','UNPR']: return 'UNPR 🦅'
    else: return party
    
def get_photo(name,names,allegiance_type2):
    if allegiance_type2=='name':
        return names[name]['Photo']
    else:
        if name in party_image_links:
            return master_image_path+party_image_links[name]
        else:
            return ''
        
def get_photos(df,names,allegiance_type2):
    photos=[]
    for i in df['name2'].values:
        photos.append(get_photo(i,names,allegiance_type2))
    df['image']=photos
    df=df[list(df.columns[:2])+list([df.columns[-1]])+list(df.columns[2:-1])]
    return df

def get_url(name,names,allegiance):
    if allegiance=='name':
        return names[name]['meta']['url']
    else:
        return ''
    
from colorthief import ColorThief

def party_color(party,default_color="#000000"):
    if party in party_image_links:
        path='ep/img/'+party_image_links[party]
        color_thief = ColorThief(path)
        rgb_color=color_thief.get_color(quality=1)        
        return '#%02x%02x%02x' % rgb_color
    else:
        return default_color
    
party_image_links={
    "ALDE":"alde.jpg",
    "ECR":"ecr.jpg",
    "ENF":"enf.jpg",
    "N/A":"independent.png",
    "EPP":"epp.jpg",
    "S&D":"S&D.png",
    "Greens":"greens.png",
    "ALDE RO":"aldero.jpg",
    "DK":"dk.png",
    "Egyéb":"hun.jpg",
    "Együtt PM":"egyutt.jpg",
    "FDGR":"fdgr.jpg",
    "FIDESZ-KDNP":"fidesz.png",
    "Jobbik":"jobbik.png",
    "LMP":"lmp.jpg",
    "MSZP":"mszp.png",
    "PMP":"pmp.png",
    "PNL":"pnl.png",
    "PNȚCD":"pntcd.png",
    "PRM":"prm.png",
    "PSD":"psd.png",
    "RMDSZ":"rmdsz.jpg",
    "UNPR":"unpr.jpg"
    }

master_image_path='https://szekelydata.csaladen.es/ep/ep/img/'
    
party_color_links={}
for party in party_image_links:
    party_color_links[party]=party_color(party)
    
def get_link_color(party,default_color="#000000"):
    if party=='N/A': return '#444444'
    elif party=='ENF': return '#777777'
    elif party=='ALDE RO': return '#459ccc'
    elif party=='FDGR': return '#961934'
    elif party=='Jobbik': return '#3cb25a'
    elif party in party_color_links:
        return party_color_links[party]
    else:
        return default_color


 