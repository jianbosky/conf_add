global
        log 127.0.0.1 local2
        daemon
        maxconn 256
        log 127.0.0.1 local2 info
defaults
        log global
        mode http
        timeout connect 5000ms
        timeout client 50000ms
        timeout server 50000ms
        option  dontlognull

listen stats :8888
        stats enable
        stats uri       /admin
        stats auth      admin:1234

frontend oldboy.org
        bind 0.0.0.0:80
        option httplog
        option httpclose
        option  forwardfor
        log global
        acl www hdr_reg(host) -i www.oldboy.org
        use_backend www.oldboy.org if www

backend www.oldboy.org
        server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000

backend buy.oldboy.org
        server 100.1.7.90 100.1.7.90 weight 20 maxconn 3000