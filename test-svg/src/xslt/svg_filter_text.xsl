<?xml version="1.0" standalone="no"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

  <!-- Add DOCTYPE -->
  <xsl:template match="/">
    <xsl:text disable-output-escaping="yes">
</xsl:text>
    <xsl:apply-templates/>
  </xsl:template>

  <!--Copie vide de l'élément texte' -->
  <xsl:template match="text">
<!--     <xsl:apply-templates select="."/>-->
  </xsl:template>

  <!-- Par défaut, la copie de l'élément en entrée -->
  <xsl:template match="*|@*|text()">
    <xsl:copy>
      <xsl:apply-templates select="*|@*"/>
    </xsl:copy>
  </xsl:template>
</xsl:stylesheet>
