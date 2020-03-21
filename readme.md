# heroku create --addons=heroku-postgresql:hobby-basic
# git push heroku master .. push git repo to heroku remote
# heroku addons:create scheduler:standard
# heroku addons:open scheduler
# add "python update_db_daily.py" to webpage

# to remove old domains
heroku domains
heroku domains:remove techwalkme.com
heroku domains:remove www.techwalkme.com

# to add domains 
# heroku domains
# heroku domains:add www.techwalkme.com
# heroku domains -- to check CNAME record
# add CName record to godaddy
# remember to add techwalkme to forwarding section in godaddy so both www.techwalkme  and techwalme work 

