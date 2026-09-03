#!/usr/bin/env python3
"""Creates seoul_attractions.csv in the current directory.

This script writes a deterministic, cleaned CSV of Seoul attractions.
If you already have a scraper, you can replace contents or use this as a fallback.
"""
import csv

DATA = [
    (1,"Gyeongbokgung Palace","Palace","Jongno","161 Sajik-ro",37.579617,126.977041,"Historic Joseon dynasty palace and major landmark.","https://english.visitkorea.or.kr","public sources"),
    (2,"Changdeokgung Palace and Huwon","Palace","Jongno","99 Yulgok-ro",37.579449,126.991045,"UNESCO World Heritage palace with secret garden (Huwon).","https://english.visitkorea.or.kr","public sources"),
    (3,"Bukchon Hanok Village","Traditional Village","Jongno","Bukchon-ro",37.582604,126.983006,"Traditional hanok neighborhood with cultural experience.","https://english.visitkorea.or.kr","public sources"),
    (4,"Insadong Cultural Street","Market/Japan","Jongno","Insadong-gil",37.574389,126.985070,"Art galleries, tea houses, traditional crafts and souvenirs.","https://english.visitkorea.or.kr","public sources"),
    (5,"Myeongdong Shopping Street","Shopping","Jung","Myeongdong",37.560975,126.986548,"Major shopping and street-food district.","https://english.visitkorea.or.kr","public sources"),
    (6,"Namsan Seoul Tower (N-Seoul Tower)","Observation/Garden","Jung","105 Namsangongwon-gil",37.551169,126.988226,"Iconic tower with city views and observatory.","https://www.seoultower.co.kr","public sources"),
    (7,"Cheonggyecheon Stream","Park/Junction","Jongno/Central","Cheonggyecheon",37.570028,126.986072,"Restored urban stream, promenades and events.","https://english.visitkorea.or.kr","public sources"),
    (8,"Dongdaemun Design Plaza (DDP)","Culture/Design","Jung","281 Eulji-ro",37.566295,127.009386,"Futuristic design complex and exhibition space.","https://www.ddp.or.kr","public sources"),
    (9,"Dongdaemun Market","Market","Jung","Dongdaemun",37.569328,127.009432,"Large shopping district open late-night.","https://english.visitkorea.or.kr","public sources"),
    (10,"Namdaemun Market","Market","Jung","12 Namdaemun-ro",37.559617,126.977041,"Historic traditional market with diverse stalls.","https://english.visitkorea.or.kr","public sources"),
    (11,"COEX Mall & Aquarium","Shopping/Aquarium","Gangnam","513 Yeongdong-daero",37.512682,127.058739,"Large underground mall and aquarium in Gangnam.","https://www.coexcenter.com","public sources"),
    (12,"Lotte World (theme park)","Attraction","Jongno/Lotte","240 Olympic-ro",37.512048,127.098632,"Indoor and outdoor amusement park with shopping.","https://www.lotteworld.com","public sources"),
    (13,"Hangang (Han River) Park - Yeouido","Park","Yeongdeungpo","Yeouido Hangang Park",37.525999,126.924678,"Large riverside park popular for cycling and picnics.","https://english.visitkorea.or.kr","public sources"),
    (14,"Seoul Forest","Park/Arts","Seongdong","273 Ttukseom-ro",37.544545,127.037556,"Large park with green areas, deer enclosure and galleries.","https://english.visitkorea.or.kr","public sources"),
    (15,"Bukhansan National Park","Nature","Bukhan","Coordinates vary",37.658409,126.988205,"Mountain park with hiking trails and scenic views.","https://english.visitkorea.or.kr","public sources"),
    (16,"National Museum of Korea","Museum","Yongsan","137 Seobinggo-ro",37.523984,126.980355,"Korea's flagship museum with large collections.","https://www.museum.go.kr","public sources"),
    (17,"War Memorial of Korea","Museum","Yongsan","29 Itaewon-ro",37.536125,126.977045,"Extensive exhibits covering Korea's military history.","https://www.warmemo.or.kr","public sources"),
    (18,"Itaewon Shopping & Food","District","Yongsan","Itaewon-dong",37.534722,126.994167,"International district with dining and nightlife.","https://english.visitkorea.or.kr","public sources"),
    (19,"Gwangjang Market","Market","Jongno","88 Changgyeonggung-ro",37.570267,126.998757,"Traditional market famous for street food like bindaetteok.","https://english.visitkorea.or.kr","public sources"),
    (20,"Hongdae (Hongik University) District","Nightlife/Arts","Mapo","Hongik University area",37.556264,126.923923,"Youthful area with clubs, street performances, cafes.","https://english.visitkorea.or.kr","public sources"),
    (21,"Olympic Park","Park/Sculpture","Gangdong","424 Olympic-ro",37.516330,127.121380,"Huge park with sculpture park and walking trails.","https://english.visitkorea.or.kr","public sources"),
    (22,"Seoul Museum of History","Museum","Jongno","Sejong-daero 55",37.572914,126.965764,"Museum covering Seoul’s history and development.","https://english.visitkorea.or.kr","public sources"),
    (23,"Seodaemun Prison History Hall","Museum","Seodaemun","251 Tongil-ro",37.576111,126.953333,"Historic site and museum on modern Korean history.","https://english.visitkorea.or.kr","public sources"),
    (24,"Ewha Womans University Shopping Street","Shopping","Seodaemun","Ewha area",37.565232,126.938110,"Student shopping street with boutiques and cafes.","https://english.visitkorea.or.kr","public sources"),
    (25,"Seongsu-dong (Cafe & Design District)","Design/Neighborhood","Seongdong","Seongsu-dong",37.544176,127.055230,"Industrial-turned-creative neighborhood with cafes and studios.","https://english.visitkorea.or.kr","public sources"),
]

OUTFILE = "seoul_attractions.csv"

def write_csv(outfile=OUTFILE):
    fieldnames = ["id","name","category","district","address","latitude","longitude","description","website","source"]
    with open(outfile, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for row in DATA:
            writer.writerow(row)
    print(f"Wrote {len(DATA)} rows to {outfile}")

if __name__ == "__main__":
    write_csv()
