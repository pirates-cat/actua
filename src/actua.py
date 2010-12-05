# -*- coding: utf-8 -*-
"""
actua: pàgina de promoció de mini-accions pirates
"""

from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

class MainPage(webapp.RequestHandler):
    def get(self):
        accions = [
                   ('1 clic', [
                        ('Uneix-te com activista pirata', """Si pots dedicar uns minuts a la setmana, necessitem gent per estendre la nostra presència al carrer i a Internet.<br><br>
                            Per coordinar-nos, envia\'ns el teu correu electrònic per enrolar-te!<br>
                            <form id="enrolat" name="enrolat" method="POST" action="/enrolat">
                                <label for="correu">Correu:</label>
                                <input type="text" id="correu" name="correu">
                                <input type="submit" value="Uneix-te">
                            </form>"""),
                        ('Segueix-nos a Facebook', self.facebook()),
                        ('Comparteix-nos a Facebook', 'Amb un sol clic pots compartir la <a href="http://www.facebook.com/share.php?u=http://www.facebook.com/pirata.cat">nostra plana a Facebook</a> i la <a href="http://www.facebook.com/share.php?u=http://pirata.cat/">nostra web</a>.'),
                        ('Segueix-nos a Twitter', self.twitter_follow()),
                        ('Dóna\'ns suport amb un tweet', self.tweet()),
                        ('Uneix-te als grups regionals', self.regionals()),
                        ('Fes-te amic del Capità Pirata a Facebook', 'El nostre estimat <a href="http://www.facebook.com/capita.pirata">capità</a> t\'espera per unir-te a nosaltres!')
                        ]),
                   ('2 clics', [
                        ('Fes ús del sistema de participació ciutadana!', 'Vota a les diferents propostes i envia les teves a: <a href="https://xifrat.pirata.cat">https://xifrat.pirata.cat</a>'),
                        ('Reenvia els nostres videos als teus amics', self.videos()),
                        ('Vota\'ns a Voota', 'Registra\'t amb el teu compte Facebook i vota per <a href="http://voota.cat/partit/PIRATA-CAT">Pirates de Catalunya</a> i els nostres caps de llistes: <a href="http://voota.cat/politic/Xavier-Vila">Xavi Vila</a>, <a href="http://voota.cat/politic/Jover-Padró">Josep Jover</a>, <a href="http://voota.cat/politic/Ester-Galimany">Ester Galimany</a> i <a href="http://voota.cat/politic/García-Fornells">Daniel García</a>.'),
                        ('Posa "PIRATA.CAT" com ideologia política al teu perfil de Facebook', 'Només cal que vagis a <a href="http://www.facebook.com/editprofile.php">Editar el meu perfil</a>.'),
                        ('Inscriu-te a <a href="http://twit.cat/">Twit.cat</a>', 'Si tens Twitter i ja ens segueixes, registrant el teu compte a Twit.cat farà que guanyem ressó. Només cal que facis follow a @twitpuntcat i t\'apuntis a la seva <a href="http://twit.cat">web</a>, dalt a la dreta.'),
                        ('Afegeix el logo de Pirates de Catalunya al teu avatar de Twitter o Facebook', 'Entra a <a href="http://twibbon.com/join/Pirates-de-Catalunya">Twibbon</a> i segueix els passos.')
                        ]),
                    ('3 clics', [
                        ('Afilia\'t', 'L\'afiliació és gratuïta, compatible amb altres afiliacions polítiques i et permetrà participar en la democràcia directa al Parlament. Omple el <a href="https://xifrat.pirata.cat/ca/alta_afiliats">formulari</a> i uneix-te!'),
                        ('Convida a tots els teus amics a fer-se seguidors de la nostra plana a Facebook', 'Ves a <a href="http://facebook.com/pirata.cat">http://facebook.com/pirata.cat</a>, a sota del logo, fes click a "Suggereix-ho a amistats". Un cop oberta la finestreta a on apareixen els teus amics, a la barra d\'adreces del navegador posa: javascript:fs.select_all(); i prem enter. Acte seguit, fes click a "Envia les invitacions".'),
                        ('Canvia el teu avatar', 'Si vols un avatar 100% PIRATA.CAT, fes servir aquest!<br><br><img src="/img/pirata_favicon.png"><br><br>Pots guardar la imatge i pujar-la com avatar a on vulguis. Pots accedir directament a les opcions de <a href="http://www.facebook.com/editprofile.php?sk=picture">Facebook</a> i <a href="http://twitter.com/settings/profile">Twitter</a> des d\'aquests enllaços.'),
                        ('Fes noves propostes al Sistema de Participació Ciutadana', 'Un cop estiguis afiliat, entra a fer propostes al <a href="https://xifrat.pirata.cat/">SPC</a> per portar-les al Parlament!')
                        ]),
                   ('Més de 3 clics', [
                        ('Enviar mails als teus amics', 'Corre la veu entre els teus amics, explica\'ls-hi què és Pirates de Catalunya per tu.<br><br>Aquí tens un <a href="/exemple_mail_pirata">exemple</a>!'),
                        ('Xarxa Wifi pirata', 'Canvia el nom de la teva xarxa (SSID) a PIRATA.CAT.'),
                        ('Vine a les reunions', 'Dimecres a les 19:30 i Diumenge a les 16:00 a <a href="http://bit.ly/riereta">C/ Riereta, 5</a>.'),
                        ])
                   ]
        
        self.response.out.write(template.render('index.html', {'accions': accions, 'proposta_enviada': self.request.get('ok') == '1', 'activista_enviat': self.request.get('ok') == '2'}))
        
    def facebook(self):
        #return '<iframe src="http://www.facebook.com/plugins/like.php?href=http%3A%2F%2Ffacebook.com%2Fpirata.cat&amp;layout=standard&amp;show_faces=true&amp;width=450&amp;action=like&amp;font=arial&amp;colorscheme=light&amp;height=80&amp;connections=30" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:450px; height:80px;" allowTransparency="true"></iframe>'
        return '<iframe src="http://www.facebook.com/plugins/likebox.php?href=http%3A%2F%2Ffacebook.com%2Fpirata.cat&amp;width=677&amp;colorscheme=light&amp;connections=24&amp;stream=false&amp;header=false&amp;height=255" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:702px; height:255px;" allowTransparency="true"></iframe>'
    
    def twitter_follow(self):
        return '<span id="follow-twitterapi"></span>'
    
    def tweet(self):
        return """<a href="http://twitter.com/share" class="twitter-share-button" data-text="Actua, pirata! A l'abordatge del Parlament! #28N #eleccions" data-count="horizontal" data-via="partit_pirata">Tweet</a><script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script>"""

    def videos(self):
        return """
        Tenim presència a diferents llocs:
        <ul>
            <li><a href="http://www.youtube.com/user/PiratesdeCatalunyaTV">Youtube</a></li>
            <li><a href="http://vimeo.com/PiratesTV">Vimeo</a></li>
            <li><a href="http://www.dailymotion.com/PiratesdeCatalunyaTV">DailyMotion</a></li>
        </ul>
        """
    
    def regionals(self):
        return """
        Visita el <a href="/directori">directori de grups regionals</a> i afegeix-te al teu. Si no el trobes, no dubtis en crear-lo i avisar-nos al Facebook de PIRATA.CAT o Twitter!
        """

class Proposta(db.Model):
    titol = db.StringProperty()
    clics = db.StringProperty()
    descripcio = db.StringProperty(multiline=True)

class Activista(db.Model):
    correu = db.StringProperty()

class Propostes(webapp.RequestHandler):
    def post(self):
        proposta = Proposta()
        
        proposta.titol = self.request.get('titol')
        proposta.clics = self.request.get('clics')
        proposta.descripcio = self.request.get('proposta')
        
        proposta.put()
        self.redirect('/?ok=1')

class Enrolament(webapp.RequestHandler):
    def post(self):
        activista = Activista()
        
        activista.correu = self.request.get('correu')
        activista.put()
        
        self.redirect('/?ok=2')

class Directori(webapp.RequestHandler):
    def get(self):
        grups = [
            ('Anoia', [
                '<a href="http://twitter.com/pirates_anoia">Twitter: @pirates_anoia</a>',
                '<a href="http://www.facebook.com/pages/Pirates-de-LAnoia/172841996063494">Facebook</a>'
            ]),
            ('Girona', [
                '<a href="http://twitter.com/Pirates_Girona">Twitter: @pirates_girona</a>'
            ]),
            ('L\'Hospitalet de Llobregat', [
                '<a href="http://www.facebook.com/pages/Pirates-de-LHospitalet-de-Llobregat/162672767097093">Facebook</a>'
            ]),
            ('Lleida', [
                '<a href="http://twitter.com/pirates_lleida">Twitter: @pirates_lleida</a>',
                '<a href="http://www.facebook.com/pages/Pirates-a-Lleida/161581270540623">Facebook</a>'
            ]),
            ('Maresme', [
                '<a href="httpe ://twitter.com/pirates_maresme">Twitter: @pirates_maresme</a>',
                '<a href="http://www.facebook.com/pages/Pirates-dEl-Maresme/166974373331221">Facebook</a>'
            ]),
            ('Ribera d\'Ebre', [
                '<a href="http://www.facebook.com/pages/Pirates-de-la-Ribera-dEbre/162200623810378">Facebook</a>',
                '<a href="http://piratesribera.wordpress.com/">Bloc</a>'
            ]),
            ('Sant Boi de Llobregat', [
                '<a href="http://www.facebook.com/pages/Pirates-de-Sant-Boi-de-Llobregat/162904380408519">Facebook</a>'
            ]),
            ('Terrassa', [
                '<a href="http://www.facebook.com/pages/Pirates-de-Terrassa/108539912547318">Facebook</a>'
            ])
        ]
        
        self.response.out.write(template.render('directori.html', { 'grups': grups }))

class ExempleMailPirata(webapp.RequestHandler):
    def get(self):        
        self.response.out.write(template.render('exemple_mail_pirata.html', { }))

"""
Totes les URLs es configuren a app.yaml, sobretot per indicar si tenen seguretat o no.
"""
application = webapp.WSGIApplication([
    ('/', MainPage),
    ('/proposa', Propostes),
    ('/enrolat', Enrolament),
    ('/directori', Directori),
    ('/exemple_mail_pirata', ExempleMailPirata)
], debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
