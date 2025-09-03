# link searcher
# Copyright (C) 2025 Douglas Barbosa
#
# Este programa é software livre: você pode redistribuí-lo e/ou modificá-lo
# sob os termos da Licença Pública Geral GNU publicada pela Free Software Foundation,
# na versão 3 da Licença, ou (a seu critério) qualquer versão posterior.
#
# Este programa é distribuído na esperança de que seja útil,
# mas SEM QUALQUER GARANTIA; sem mesmo a garantia implícita de
# COMERCIABILIDADE ou ADEQUAÇÃO A UM DETERMINADO PROPÓSITO.
# Consulte a Licença Pública Geral GNU para mais detalhes.
#
# Você deve ter recebido uma cópia da Licença Pública Geral GNU
# junto com este programa. Se não, veja <https://www.gnu.org/licenses/>.
#
# ----------------------------------------------------------------------------
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


import requests
# import inspect
from bs4 import BeautifulSoup

class Page:
    def __init__(self, link):
        self.link = link 
        self.request = None  

    def check_page(self): # See if the code can reach the page
        try:
            self.request = requests.get(self.link, timeout=5)  # try acess
            self.request.raise_for_status()  # check status
            print(f'Page acess OK: {self.request.status_code}')
            self.soup = BeautifulSoup(self.request.text, 'html.parser')
            return True
        except requests.exceptions.RequestException as err:
            print('Error:',
                  f'\n{err}')
            return False      

    def search_download_methods(self): # Show the downloads avaible in archive
        download_section = self.soup.find("section", class_="boxy item-download-options")

        if download_section:
            links = download_section.find_all("a", class_="format-summary download-pill")

            # Take the download itens
            hrefs = []
            for link in links:
                href = "https://archive.org" + link["href"]
                hrefs.append(href)

            return hrefs
        else:
            print("Download Section not found.")
            return None  # Grant that somethings is returned

    def download_link(self):
        if self.check_page():
            return self.search_download_methods() 
        elif self.check_page() == False:
            print(f"Couldn't reach the download methods")
            return None


page = Page



def main(page_link):
    page = Page(page_link).download_link()
    if page:
        index = 0
        link_arr = []
        for link in page:
            print(f'{index}: {link}')
            index += 1
            link_arr.append(link)
        return link_arr
    else:
        return "No link found or error accessing the page!"
    


