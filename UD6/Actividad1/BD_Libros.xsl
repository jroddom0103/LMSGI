<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" 
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:output method="html" encoding="UTF-8"/>

<xsl:template match="/Libros">

    <html>
        <head>
            <style type="text/css">
            
            td, th{
                border: black 1px solid;
            }

            </style>
        </head>  

        <body>

            <table style="border-collapse: collapse; margin: 0 auto;">

                <tr>

                    <th>Cod_Libro</th>
                    <th>Titulo</th>
                    <th>Cod_Autor</th>
                    <th>Editorial</th>
                    <th>Edicion</th>
                    <th>ISBN</th>
                    <th>NumPáginas</th> 

                </tr>

                <xsl:for-each select="libro">
                
                
            
                <tr>
                    <td><xsl:value-of select="Cod_Libro"/></td>
                    <td><xsl:value-of select="Titulo"/></td>
                    <td><xsl:value-of select="Autores/autor/Cod_Autor"/></td>
                    <td><xsl:value-of select="Editorial"/></td>
                    <td><xsl:value-of select="Edicion"/></td>
                    <td><xsl:value-of select="ISBN"/></td>
                    <td><xsl:value-of select="NumPaginas"/></td>

                </tr>

            </xsl:for-each>

           

            </table>

            <table style="border-collapse: collapse; margin: 0 auto;">

                <tr>

                    <th>Cod_Autor</th>
                    <th>Nombre</th>
                    <th>Apellidos</th>
                    <th>Fecha Nacimiento</th>

                </tr>

                <xsl:for-each select="libro">
                
                
                <tr>
                    <td><xsl:value-of select="Autores/autor/Cod_Autor"/></td>
                    <td><xsl:value-of select="Autores/autor/Nombre"/></td>
                    <td><xsl:value-of select="Autores/autor/Apellidos"/></td>
                    <td><xsl:value-of select="Autores/autor/FechaNacimiento"/></td>
                </tr>

            </xsl:for-each>

            </table>


        </body>


    </html>


</xsl:template>

</xsl:stylesheet>



    







    
