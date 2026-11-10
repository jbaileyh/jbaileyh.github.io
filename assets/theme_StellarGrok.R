# StellarGrok chart styling for ggplot2.
# Usage in a post (hidden setup chunk):
#   source("../../../assets/theme_StellarGrok.R")

fn_cols <- c(
  forest = "#08251a", forest_500 = "#197050", lime = "#abff44", leaf = "#3ab533",
  sage_50 = "#eff6e9", sage_200 = "#d8e4cb", sage_500 = "#717863",
  mint = "#2f9b99", pink = "#c96384", gold = "#e0a526"
)
fn_palette <- unname(fn_cols[c("forest_500", "mint", "pink", "gold", "leaf", "forest")])

theme_StellarGrok <- function(base_size = 13) {
  ggplot2::theme_minimal(base_size = base_size) +
    ggplot2::theme(
      plot.title.position = "plot",
      plot.title = ggplot2::element_text(face = "bold", colour = fn_cols[["forest"]], size = base_size * 1.25),
      plot.subtitle = ggplot2::element_text(colour = fn_cols[["sage_500"]]),
      plot.caption = ggplot2::element_text(colour = fn_cols[["sage_500"]], hjust = 0),
      axis.text = ggplot2::element_text(colour = fn_cols[["forest"]]),
      axis.title = ggplot2::element_text(colour = fn_cols[["forest"]]),
      panel.grid.major = ggplot2::element_line(colour = fn_cols[["sage_200"]], linewidth = 0.4),
      panel.grid.minor = ggplot2::element_blank(),
      legend.position = "top",
      legend.justification = "left",
      strip.text = ggplot2::element_text(face = "bold", colour = fn_cols[["forest"]], hjust = 0)
    )
}

scale_colour_StellarGrok <- function(...) ggplot2::scale_colour_manual(values = fn_palette, ...)
scale_fill_StellarGrok   <- function(...) ggplot2::scale_fill_manual(values = fn_palette, ...)

ggplot2::theme_set(theme_StellarGrok())
