# gobuster-bad-website
A demo website with vulnerabilities to test out go buster

# Serve bad website
1. Build the docker container<br>
```dockerfile
docker build -t bad-website .
```
1. Run the docker container. <PORT> can be whatever port of your choosing<br>
```dockerfile
docker run -d -p <PORT>:8000 bad-website
```
1. Visit `localhost:<PORT>`