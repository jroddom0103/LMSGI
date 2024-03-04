<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
    <body>
        <h1>Discos de música</h1>
        <table bgcolor="#775522">
            <tr bgcolor="#885588">
                <th>Título del Álbum</th>
                <th>Artista</th>
                <th>Título de la canción 1</th>  
                <th>Título de la canción 2</th>
                <th>Sello Discográfico</th>
                <th>Año de Publicación</th>  
            </tr>    
            <xsl:for-each select="cds/cd">
            <tr>
                <td><xsl:value-of select="tituloAlbum"/></td>
                <td><xsl:value-of select="artista"/></td>
                <td><xsl:value-of select="tituloCancion"/></td>
                <td><xsl:value-of select="tituloCancion2"/></td>
                <td><xsl:value-of select="selloDiscografico"/></td>
                <th><xsl:value-of select="añoPublicacion"/></th>
            </tr>    
            </xsl:for-each>
        </table>
    </body>
</html>
</xsl:template>
</xsl:stylesheet>