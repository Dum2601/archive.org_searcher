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

from flask import Blueprint, request, jsonify
from utils.URL_operations.get_page import main

# Define o blueprint
routes_bp = Blueprint('routes', __name__)

download_links = []


@routes_bp.route('/get_link_page', methods=['POST'])
def get_page_link():
    data = request.get_json()
    if not data or 'link' not in data:
        return jsonify({"error": "Missing 'link' in request"}), 400
    link = data['link']
    global download_links
    download_links = main(link)
    return jsonify({"message": "Links obtained successfully", "links": download_links})



