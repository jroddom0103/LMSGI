<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
    <body>
        <h1>Discos de música</h1>
        <table bgcolor="#775522">
            <tr bgcolor="#885588">
                <th>Artista</th>
                <th>Título de la canción 1</th>  
                <th>Título de la canción 2</th>  
            </tr>    
            <xsl:for-each select="cds/cd">
            <xsl:if test="artista='Artista1'">
            <tr>
                <td><xsl:value-of select="artista"/></td>
                <td><xsl:value-of select="tituloCancion"/></td>
                <td><xsl:value-of select="tituloCancion2"/></td>
            </tr>    
            </xsl:if>
            </xsl:for-each>
        </table>
    </body>
</html>
</xsl:template>
</xsl:stylesheet>
