UPDATE activity SET checkout = DATETIME(checkin, '+1 hour') WHERE checkin IS NOT NULL AND checkout IS NULL;
.quit