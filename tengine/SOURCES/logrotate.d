/var/log/nginx/*log {
    daily
    dateext
    rotate 30
    maxage 30
    missingok
    notifempty
    sharedscripts
    delaycompress
    postrotate
        /sbin/service nginx reload > /dev/null 2>/dev/null || true
    endscript
}
