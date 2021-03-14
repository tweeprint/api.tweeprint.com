user="alex"
host="api.tweeprint.com"

# Empty the current source directory on the server
ssh $user@$host "rm -r ~/$host/source/* >& /dev/null"

# Send git tracked files
rsync -vr . --exclude-from='.gitignore' --exclude='.git' $user@$host:~/$host/source

# Copy secrets
scp core/secrets.py $user@$host:~/$host/source/core/secrets.py

# Turn off debug on server
ssh $user@$host "sed -i s/\"DEBUG = True\"/\"DEBUG = False\"/g ~/$host/source/core/settings.py"

# Add allowed host
ssh $user@$host "sed -i s/\"HOSTS = \[\]\"/\"HOSTS = \['.$host'\]\"/g ~/$host/source/core/settings.py"

# Switch database
ssh $user@$host "sed -i s/\"DATABASES = local\"/\"DATABASES = live\"/g ~/$host/source/core/secrets.py"

# Install pip packages
ssh $user@$host "~/$host/env/bin/pip install docupy"
ssh $user@$host "~/$host/env/bin/pip install django_admin_reset"
ssh $user@$host "~/$host/env/bin/pip install rcssmin --install-option="--without-c-extensions""
ssh $user@$host "~/$host/env/bin/pip install libsass"
ssh $user@$host "~/$host/env/bin/pip install psycopg2-binary"
ssh $user@$host "~/$host/env/bin/pip install -r ~/$host/source/requirements.txt"

# Apply migrations
ssh $user@$host "~/$host/env/bin/python ~/$host/source/manage.py migrate"

# Move static files
ssh $user@$host "cd ~/$host/source && ../env/bin/python manage.py compilescss"
ssh $user@$host "cd ~/$host/source && ../env/bin/python manage.py collectstatic --noinput"
