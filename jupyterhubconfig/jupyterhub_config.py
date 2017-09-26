# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

# Configuration file for JupyterHub
import os

c = get_config()

# We rely on environment variables to configure JupyterHub so that we
# avoid having to rebuild the JupyterHub container every time we change a
# configuration parameter.
# User containers will access hub by container name on the Docker network
#c.JupyterHub.hub_ip = 'jupyterhub'
#c.JupyterHub.hub_port = 8000

# TLS config
#c.JupyterHub.port = 443
#c.JupyterHub.ssl_key = os.environ['SSL_KEY']
#c.JupyterHub.ssl_cert = os.environ['SSL_CERT']

#Add admin user
#c.Authenticator.admin_users = {'lorenzo'}
#c.Authenticator.admin_users = {'rhea','lorenzo'}

#Proxy authentication token
c.JupyterHub.proxy_auth_token = '0bc02bede919e99a26de1e2a7a5aadfaf6228de836ec39a05a6c6942831d8fe5'
#ConfigurableHTTPProxy.auth_token = '0bc02bede919e99a26de1e2a7a5aadfaf6228de836ec39a05a6c6942831d8fe5'

# Set the log level by value or name.
c.JupyterHub.log_level = 'DEBUG'

# Enable debug-logging of the single-user server
c.Spawner.debug = True


#Postgres Config
c.JupyterHub.db_url = 'postgresql://{user}:{password}@{host}/{db}'.format(
    host=os.environ['POSTGRES_HOST'],
    password=os.environ['POSTGRES_PASSWORD'],
    db=os.environ['POSTGRES_DB'],
    user=os.environ['POSTGRES_USER']
)




# jupyterhub config file
#
c.JupyterHub.authenticator_class = 'ldapcreateusers.LocalLDAPCreateUsers'
#c.LocalLDAPCreateUsers.server_address = 'some.ldap.server'
#c.LocalLDAPCreateUsers.server_port = 389
#c.LocalLDAPCreateUsers.use_ssl = False
#c.LocalLDAPCreateUsers.bind_dn_template = 'uid={username},dc=yourdomain,dc=com'
c.LocalLDAPCreateUsers.create_system_users = True


# Ldap configuration
#Enable Ldap auth
#c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'

#ldap Server config
c.LDAPAuthenticator.server_address = '192.168.0.29'
c.LDAPAuthenticator.use_ssl = True
c.LDAPAuthenticator.server_port = 636
c.LDAPAuthenticator.bind_dn_template = 'uid={username},cn=users,cn=accounts,dc=daf,dc=gov,dc=it'
#c.LDAPAuthenticator.lookup_dn = True
#c.LDAPAuthenticator.lookup_dn_search_filter = '({uid}={login})'
#c.LDAPAuthenticator.lookup_dn_search_user = 'cn=admins,cn=groups,cn=accounts,dc=daf,dc=gov,dc=it'
#c.LDAPAuthenticator.lookup_dn_search_password = 'uWae6wae'
#c.LDAPAuthenticator.user_search_base = 'cn=users,cn=accounts,dc=daf,dc=gov,dc=it'
#c.LDAPAuthenticator.user_attribute = 'uid'
#c.LDAPAuthenticator.lookup_dn_user_dn_attribute = 'cn'
# GROUP
#c.LDAPAuthenticator.allowed_groups = [
#    'cn=jupyterhub_admin,cn=groups,cn=accounts,dc=daf,dc=gov,dc=it'
#]
#    'cn=researcher,ou=groups,dc=wikimedia,dc=org',
#    'cn=operations,ou=groups,dc=wikimedia,dc=org'
#]


# LDAPAuthenticator.lookup_dn: Whether to try a reverse lookup to obtain the user's DN. Some LDAP servers, such as Active Directory, don't always bind with the true DN, so this allows us to discover it based on the username.
#c.LDAPAuthenticator.lookup_dn = True

#LDAPAuthenticator.user_search_base: Only used with lookup_dn=True. Defines the search base for looking up users in the directory.
#c.LDAPAuthenticator.user_search_base = 'ou=People,dc=example,dc=com'

#LDAPAuthenticator.user_attribute: Only used with lookup_dn=True. Defines the attribute that stores a user's username in your directory.
# Active Directory
#c.LDAPAuthenticator.user_attribute = 'sAMAccountName'

# OpenLDAP
#c.LDAPAuthenticator.user_attribute = 'uid'


# in jupyterhub_config.py
#from jupyterhub.spawner import LocalProcessSpawner

#class SameUserSpawner(LocalProcessSpawner):
#    """Local spawner that runs single-user servers as the same user as the Hub itself.
#
#    Overrides user-specific env setup with no-ops.
#    """
#    
#    def make_preexec_fn(self, name):
#        """no-op to avoid setuid"""
#        return lambda : None
#    
#    def user_env(self, env):
#        """no-op to avoid setting HOME dir, etc.""" 
#        return env

#c.JupyterHub.spawner_class = SameUserSpawner

c.Authenticator.admin_users = {'rhea','pippo'}
#c.Authenticator.whitelist = {'lorenzo', 'pippo'}

c.JupyterHub.admin_access = True

#c.LocalAuthenticator.create_system_users = True

# jupyterhub config file


# TLS config
#c.JupyterHub.port = 443
#c.JupyterHub.ssl_key = os.environ['SSL_KEY']
#c.JupyterHub.ssl_cert = os.environ['SSL_CERT']
